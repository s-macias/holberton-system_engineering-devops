# puppet script to fix a typo in a configuration wordpress file
exec { 'fix':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
