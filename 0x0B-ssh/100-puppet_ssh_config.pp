# setup an ssh configuration file
file { '/etc/ssh/ssh_config':
    ensure => 'file',
    mode   => '0644',
}

augeas { '/etc/ssh/ssh_config':
    context => '/files/etc/ssh/ssh_config',
    changes => [
    'set Host[. = "525397-web-01"]',
    'set Host/HostName "54.175.225.156"',
    'set Host/User "ubuntu"',
    'set Host/IdentityFile "~/.ssh/school"',
    'set Host/IdentitiesOnly "yes"',
    'set Host/PasswordAuthentication "no"',
  ],
}
