from constance import config


def show_system_content(request):
    return {
        'config': config
    }
