# creating a file
file{'/tmp/holberton':
ensure   => 'file',
path     => '/tmp/holberton',
owner    => 'www-data',
group    => 'www-data',
mode     => '0744',
content  => 'I love Puppet\n'
}
