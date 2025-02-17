# added custom http header to include hostname
package { 'nginx':
    ensure   => installed,
    provider => apt
}

exec { 'allow HTTP':
    command => 'sudo ufw allow "Nginx HTTP"',
    path    => ['/usr/sbin/', '/bin/', '/sbin/']
}

exec { 'set the header text':
    command => "sudo sed -i '0,/try_files \\$uri \\$uri\\/ =404;/s/try_files \\$uri \\$uri\\/ =404;/try_files \\$uri \\$uri\\/ =404; \\n add_header X-Served-By \"${hostname}\";/' /etc/nginx/sites-available/default",
    path    => ['/usr/bin/', '/bin/', '/sbin/'],
    notify  => Exec['reload nginx']
}

file { '/etc/nginx/sites-available/default':
    ensure  => file,
}

file { '/var/www/html/index.html':
    ensure  => file,
    mode    => '0644',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'Hello World!',
}

exec { 'reload nginx':
    command => 'sudo service nginx start',
    path    => ['/usr/bin/', '/bin/', '/sbin/'],
    onlyif  => 'test -f /etc/nginx/sites-available/default'
}

service { 'nginx':
    ensure  => running,
    enable  => true,
}
