exec{ 'wp-settings.php':
      path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
      command  => 'sed -i -e "s/phpp/php/g" /var/www/html/wp-settings.php',
      provider => 'shell',
}