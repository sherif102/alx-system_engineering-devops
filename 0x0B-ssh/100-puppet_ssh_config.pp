# setup an ssh configuration file named ~/.ssh/school
file { '${HOME}/.ssh/ssh_config':
    ensure  => 'file',
    mode    => '0600',
    content => 'Host 525397-web-01\n\tHostName 54.175.225.156\n\tUser ubuntu\n\tIdentityFile ~/.ssh/school\n\tIdentitiesOnly yes\n\tPasswordAuthentication no',
}
