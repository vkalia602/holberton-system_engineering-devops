# kills a process
exec{ 'kill_process':
    path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
    command  => 'pkill killmenow'
    provider => 'shell',
}