# -*- coding: utf-8 -*-
from docker import Client
import time
from django.shortcuts import render,render_to_response
from django.http.response import HttpResponse
import json
'''
配置docker允许远程连接
修改vi /etc/sysconfig/docker
在OPTIONS= 后增加-H unix:///var/run/docker.sock -H tcp://0.0.0.0:2375
'''
c=Client(base_url='tcp://192.168.112.116:2375')
def index(request):
    res_data=c.info()
    return render_to_response('index.html',{'server':res_data})

def timecreate(num):
    #时间戳格式化
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(num))
sizecreate=lambda x:x/1000/1000 #计算文件大小
def getdata(request):
    data=request.GET.get('data')
    res_data=c.info()
    if data=='live':
        #计算容器数
        Containers=res_data[u'Containers']
        ContainersRunning=res_data[u'ContainersRunning']
        ContainersStopped=res_data[u'ContainersStopped']
        ContainersPaused=res_data[u'ContainersPaused']
        return HttpResponse(json.dumps([ContainersRunning,ContainersStopped,ContainersPaused,Containers]))
    
def check_container_stats(container_name,collect_item):
    container_collect=c.stats(container_name)
    old_result=eval(container_collect.next())
    new_result=eval(container_collect.next())
    container_collect.close()
    if collect_item == 'cpu_total_usage':
        result=new_result['cpu_stats']['cpu_usage']['total_usage'] - old_result['cpu_stats']['cpu_usage']['total_usage']
    elif collect_item == 'cpu_system_usage':
        result=new_result['cpu_stats']['system_cpu_usage'] - old_result['cpu_stats']['system_cpu_usage']
    elif collect_item == 'cpu_percent':
        cpu_total_usage=new_result['cpu_stats']['cpu_usage']['total_usage'] - old_result['cpu_stats']['cpu_usage']['total_usage']
        cpu_system_uasge=new_result['cpu_stats']['system_cpu_usage'] - old_result['cpu_stats']['system_cpu_usage']
        cpu_num=len(old_result['cpu_stats']['cpu_usage']['percpu_usage'])
        result=round((float(cpu_total_usage)/float(cpu_system_uasge))*cpu_num*100.0,2)
    elif collect_item == 'mem_usage':
        result=new_result['memory_stats']['usage']
    elif collect_item == 'mem_limit':
        result=new_result['memory_stats']['limit']
    elif collect_item == 'mem_percent':
        mem_usage=new_result['memory_stats']['usage']
        mem_limit=new_result['memory_stats']['limit']
        result=round(float(mem_usage)/float(mem_limit)*100.0,2)
#     elif collect_item == 'network_rx_bytes':
#         network_check_command="""sudo /usr/bin/docker exec %s cat /proc/net/dev|sed -n 3p|awk '{print $2,$10}'"""%container_name
#         result=os.popen(network_check_command).read().split()[0]
#     elif collect_item == 'network_tx_bytes':
#         network_check_command="""sudo /usr/bin/docker exec %s cat /proc/net/dev|sed -n 3p|awk '{print $2,$10}'"""%container_name
#         result=os.popen(network_check_command).read().split()[1]
    return result
def rongqi(request):
    #容器页
    logs=''
    if request.GET.get('c')!=None and request.GET.get('d')!=None:
        if request.GET.get('c')=='start': #启动容器
            status=c.start(request.GET.get('d'))
        if request.GET.get('c')=='stop': #关闭容器
            status=c.stop(request.GET.get('d'), 20)
        if request.GET.get('c')=='logs': #查看log
            logs=c.logs(request.GET.get('d'))
            return render_to_response('log.html',{'logs':logs})
        if request.GET.get('c')=='rm':
            status=c.stop(request.GET.get('d'), 20)
            status=c.remove_container(request.GET.get('d'))
        if request.GET.get('c')=='chk':
            rongqi_d=c.inspect_container(request.GET.get('d'))
            print c.stats(request.GET.get('d'),decode='--format "table {{.ID}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"',stream=False)
            
            return render_to_response('rongqi_details.html',{'rongqi_d':rongqi_d})
    docker_ps=c.containers(all=1)
    for dockerps in docker_ps:
        dockerps[u'Names']=dockerps[u'Names'][0].split('/')[1]
        dockerps[u'Created']=timecreate(dockerps[u'Created'])
    #print docker_ps

    return render_to_response('rongqi_index.html',{'server_list':docker_ps})
def images(request):
    if request.GET.get('c')!=None and request.GET.get('d')!=None:
        if request.GET.get('c')=='rmi': #删除镜像
            status=c.remove_image(request.GET.get('d'))
        if request.GET.get('c')=='chk':
            images_d=c.inspect_image(request.GET.get('d'))
            return render_to_response('image_details.html',{'images_d':images_d})
    #镜像页
    docker_images=c.images()
    for image in docker_images:
        image2={}
        if len(image[u'RepoTags'])>1:
            fenge=image[u'RepoTags'][1].split(':')
            image2[u'name']=fenge[0]
            image2[u'tag']=fenge[1]
            image2[u'Id']=image[u'Id']
            image2[u'Created']=image[u'Created']
            image2[u'Size']=image[u'Size']
            image2[u'Labels']=image[u'Labels']
            image2[u'VirtualSize']=image[u'VirtualSize']
            image2[u'ParentId']=image[u'ParentId']
            image2[u'RepoTags']=[image[u'RepoTags'][1]]
            image2[u'RepoDigests']=image[u'RepoDigests']
            docker_images.append(image2)
            
    for image in docker_images:
        image[u'Id']=image[u'Id'].split(':')[1]
        image[u'Created']=timecreate(image[u'Created'])
        image[u'Size']=sizecreate(image[u'Size'])
        fenge=image[u'RepoTags'][0].split(':')
        if len(fenge)>2:
            image[u'name']=fenge[0]+':'+fenge[1]
            image[u'tag']=fenge[2]
        else:
            image[u'name']=fenge[0]
            image[u'tag']=fenge[1]
        
    return render_to_response('images_index.html',{'image_list':docker_images})