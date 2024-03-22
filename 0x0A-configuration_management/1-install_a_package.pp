# Install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command     => 'pip3 install Flask==2.1.0',
  path        => '/usr/local/bin:/usr/bin',
  environment => ['PATH=/usr/local/bin:/usr/bin'],
  unless      => 'pip3 show Flask | grep -q "Version: 2.1.0"',
}
