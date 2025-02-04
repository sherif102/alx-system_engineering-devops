# setup an ssh configuration file named ~/.ssh/school
file { '/home/ubuntu/.ssh/ssh_config':
    ensure  => 'file',
    mode    => '0600',
    content => @("END"),
Host 525397-web-01
    HostName 54.175.225.156
    User ubuntu
    IdentityFile ~/.ssh/school
    IdentitiesOnly yes
    PasswordAuthentication no
END
}
