# puppet file to modify configuration file
# It refuses to ask for a password and adds a private key
file { 'etc/ssh/ssh_config':
    IdentityFile => '~/.ssh/holberton',
    content      => 'PasswordAuthentication no',
}
