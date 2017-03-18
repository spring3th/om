# -*- coding: utf-8 -*-
from django.shortcuts import  render,render_to_response,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from lebo.models import IDC,Host,HostDetail,HostGroup,Server,SystemType,Network

@login_required
def idc(request):
    """
    idc_list机房列表
    server :服务器
    host：主机
    :param request:
    :return:
    """
    idc_list = IDC.objects.order_by('pk')
    count = {}
    for idc in idc_list:
        num = 0
        for server in idc.server_set.all():
            num+=server.host_set.count()
        count[int(idc.id)]=num
    return render(request,'idcnet/idc.html',locals())

@login_required
def system(request):
    """
    操作系统列表
    :param request:
    :return system_list:
    """
    system_list= SystemType.objects.order_by('name')
    return render(request, 'idcnet/system.html', locals())

@login_required
def server(request):
    """
    服务器列表
    :param request:
    :return:
    """
    system_id = request.GET.get('system_id')
    idc_id = request.GET.get('idc_id')
    system_list = SystemType.objects.order_by('name')
    idc_list = IDC.objects.order_by('name')
    server_list = Server.objects.order_by('ip')
    if system_id:
        if idc_id:
            server_list = server_list.filter(ip__host__systype=system_id,idc=idc_id)
        else:
            server_list = server_list.filter(ip__host__systype=system_id)
    elif idc_id:
        server_list = server_list.filter(idc=idc_id)
    else:
        server_list = server_list
    return render(request, 'idcnet/server.html', locals())

@login_required
def host(request):
    """
    主机列表
    :param request:
    :return:
    """
    system_id = request.GET.get('system_id')
    server_id = request.GET.get('server_id')
    idc_id=request.GET.get('idc_id')
    hostname=request.POST.get('hostname')
    host_list=Host.objects.order_by('ip')
    system_list = SystemType.objects.order_by('name')
    server_list = Server.objects.order_by('name')
    idc_list = IDC.objects.order_by('name')
    #根据系统、机房、服务器过滤
    if system_id:
        if server_id:
            host_list = host_list.filter(system_type=system_id,server=server_id)
        elif idc_id:
            servers=server_list.filter(idc=idc_id)
            host_list = host_list.filter(system_type=system_id,server__in=servers)
        else:
            host_list = host_list.filter(system_type=system_id)
    elif server_id:
        host_list = host_list.filter(server=server_id)
    elif idc_id:
        servers=server_list.filter(idc=idc_id)
        host_list = host_list.filter(server__in=servers)
    else:
        host_list= host_list.order_by('ip')
    #根据主机名搜索，不区分大小写的匹配
    if hostname:
        host_list =host_list.filter(ip__tgt_id__icontains=hostname)
    else:
        host_list= host_list
    return render(request, 'idcnet/host.html', locals())


@login_required
def detail(request, ip):
    """
    主机详情
    :param request:
    :param ip:
    :return:
    """
    host_detail = HostDetail.objects.get(ip=ip)
    return render(request, 'idcnet/detail.html', {'host_detail': host_detail})

@login_required
def network(request):
    """
    网络列表
    :param request:
    :return:
    """
    idc_id = request.GET.get('idc_id')
    if idc_id:
        net_list = Network.objects.filter(idc=idc_id).order_by('name')
    else:
        net_list = Network.objects.order_by('name')
    idc_list = IDC.objects.order_by('name')
    return render(request,'idcnet/network.html',locals())
