
# puppet file to modify configuration file
# It refuses to ask for a password and adds a private key
file-line { 'etc/ssh/ssh_config':
    Path         => '~/.ssh/config',
    IdentityFile => '~/.ssh/holberton',
    line      => 'PasswordAuthentication no',
}
