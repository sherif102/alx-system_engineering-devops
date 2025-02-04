# setup an ssh configuration file named ~/.ssh/school
$text = @(END)
Host 525397-web-01
    HostName 54.175.225.156
    User ubuntu
    IdentityFile ~/.ssh/school
    IdentitiesOnly yes
    PasswordAuthentication no
END

file { 'ssh_config':
    ensure  => 'file',
    path    => '~/.ssh/school',
    content => inline_template($text),
}
