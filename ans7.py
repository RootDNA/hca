
import testinfra

def test_nginx_install(host):
    assert host.package('nginx').is_installed


def test_nginx_running(host):
    assert host.service('nginx').is_running


def test_nginx_on_port_80(host):
    assert host.socket('tcp://0.0.0.0:80').is_listening