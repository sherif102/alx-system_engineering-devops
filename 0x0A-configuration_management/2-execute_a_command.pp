# executes a kill command called killmenow
exec { 'killmenow':
    command => 'pkill killmenow',
    path    => ['/usr/bin', '/bin'],
}
