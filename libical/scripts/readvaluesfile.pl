

sub read_values_file {
  
  my $path = shift;
  my %h;

  open(F,$path) || die "Can't open values file $path";

  while(<F>){
    
    chop; 
 
    s/#.*$//g;
   
    next if ! $_;

    @column = split(/,/,$_);
    
    my $value_name = $column[0];

    my $c_type_str =  $column[1];
    my $c_autogen = ($c_type_str =~ /\(a\)/);

    my $c_type = $c_type_str;
    $c_type =~ s/\(.\)//;

    my $cpp_type =  $column[2];
    my $perl_type =  $column[3];
    my $python_type =  $column[4];
    my $components = $column[5];
    
    my @components;
    if($components ne "unitary"){
      @components = split(/;/,$components);
    } else {
      @components = ();
    }

    $h{$value_name} = { C => [$c_autogen,$c_type],
			perl => $perl_type,
			python => $python_type,
			components=>[@components]
		      };
  }

  return %h;
}

sub read_properties_file {
  
  my $path = shift;
  my %h;

  open(F,$path) || die "Can't open properties file $path";

  while(<F>){
    
    chop; 
 
    s/#.*$//g;
    s/\"//g;
   
    next if ! $_;

    @column = split(/,/,$_);
    
    my $property_name = $column[0];

    my $lic_value = $column[1];
    my $default_value = $column[2];
    
    $h{$property_name} = { lic_value => $lic_value,
			   default_value => $default_value
			 };
  }

  return %h;
}


1;