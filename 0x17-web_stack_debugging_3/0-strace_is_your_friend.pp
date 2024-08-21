# 0-strace_is_your_friend.pp

exec { 'fix-apache-permissions':
  command => 'chmod 644 /var/www/html/.htaccess && chown www-data:www-data /var/www/html/.htaccess',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'test -e /var/www/html/.htaccess',
}

service { 'apache2':
  ensure => 'running',
  enable => true,
  require => Exec['fix-apache-permissions'],
}

