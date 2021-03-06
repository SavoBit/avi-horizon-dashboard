#    Copyright 2015, Avi Networks, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf.urls import patterns
from django.conf.urls import url

from avidashboard.dashboards.project.loadbalancers import views


urlpatterns = patterns(
    'avidashboard.dashboards.project.loadbalancers.views',
    url(r'^addcertificate$', views.AddCertificateView.as_view(), name='addcertificate'),
    url(r'^associatecertificate/(?P<pool_id>[^/]+)/$',
        views.AssociateCertificateView.as_view(), name='associatecertificate'),
    url(r'^disassociatecertificate/(?P<pool_id>[^/]+)/$',
        views.DisassociateCertificateView.as_view(), name='disassociatecertificate'),
)

