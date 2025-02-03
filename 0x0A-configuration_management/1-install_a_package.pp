# install a package flask from pip3
package { ['flask', 'werkzeug']:
    ensure   => '2.1.0',
    provider => 'pip3',
}

exec { 'install_compatible_wekzeug':
    command => 'pip3 install "Werkzeug<2.1"',
    unless  => 'pip3 list | grep Werkzeug | grep 2.0',
}
