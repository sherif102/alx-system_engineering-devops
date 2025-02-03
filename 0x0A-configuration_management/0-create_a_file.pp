# creates a school in tmp with content
file { '/tmp/school' :
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
