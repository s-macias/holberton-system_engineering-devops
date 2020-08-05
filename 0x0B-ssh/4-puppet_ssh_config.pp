# puppet file to modify configuration file
# It refuses to ask for a password and adds a private key
file_line { 'etc/ssh/ssh_config':
    path         => '/etc/ssh/ssh_config',
    line         => 'IdentityFile ~/.ssh/holberton',
    line         => 'PasswordAuthentication no',
}
