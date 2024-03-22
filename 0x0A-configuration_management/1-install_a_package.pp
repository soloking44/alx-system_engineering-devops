#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package {'flask':
command     => 'pip3 install Flask==2.1.0',
path        => '/usr/local/bin:/usr/bin',
environment => ['PATH=/usr/local/bin:/usr/bin'],
  ensure   => '2.1.0',
  provider => 'pip3'
}
