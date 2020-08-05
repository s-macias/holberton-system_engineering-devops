# puppet file to modify configuration file
# It refuses to ask for a password and adds a private key
file_line { 'refuse password request':
    path         => '/etc/ssh/ssh_config',
    line         => ''PasswordAuthentication no',
}
file_line { 'private key':
    path         => '/etc/ssh/ssh_config',
    line         => 'IdentityFile ~/.ssh/holberton',
}
