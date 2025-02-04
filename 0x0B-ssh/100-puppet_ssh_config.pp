# setup an ssh configuration file named ~/.ssh/school
$text = @(END)
Host 525397-web-01
    HostName 54.175.225.156
    User ubuntu
    IdentityFile ~/.ssh/school
    IdentitiesOnly yes
    PasswordAuthentication no
END

file { '${::home}/.ssh/school':
    ensure  => 'file',
    mode    => '0600',
    content => inline_template($text),
}
