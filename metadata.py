defaults = {}

# if we install apt, install default packages
if node.has_bundle("apt"):
    defaults['apt'] = {
        'packages': {
            'cron-apt': {'installed': True},
            'curl': {'installed': True},
            'ca-certificates': {'installed': True},
            'git': {'installed': True},

            "grep": {'installed': True},
            "gzip": {'installed': True},
            "hostname": {'installed': True},
            "htop": {'installed': True},
            'tmux': {'installed': True},

            'vim': {'installed': True},
            'zsh': {'installed': True},
            'unzip': {'installed': True},
        }
    }

release_names = {
    16: {
        4: 'xenial',
        10: 'yakkety',
    },
    17: {
        4: 'zesty',
        10: 'artful',
    },
    18: {
        4: 'bionic',
        10: 'cosmic'
    },
    19: {
        4: 'disco',
        10: 'eoam',
    },
    20: {
        4: 'focal',
        10: 'groovy'
    },
    21: {
        4: 'hirsute',
    }
}

# set release_name
defaults['ubuntu'] = {
    'release_name': release_names.get(node.os_version[0], 20).get(node.os_version[1], 'focal'),
    'init': 'systemd',
}
