# Creates a manifest that kills a process
exec { 'kill killmenow':
  path    => './killmenow',
  command => 'kill killmenow',
}
