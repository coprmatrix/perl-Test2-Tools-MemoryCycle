#
# spec file for package perl-Test2-Tools-MemoryCycle (Version 0.01)
#
# Copyright (c) 124 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define cpan_name Test2-Tools-MemoryCycle
Name:           perl-Test2-Tools-MemoryCycle
Version:        0.01
Release:        0
License:   Artistic-1.0 or GPL-1.0-or-later
Summary:        Check for memory leaks and circular memory references
Url:            https://metacpan.org/release/%{cpan_name}
Source0:         https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  (rpm-build-perl or perl-generators)
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(PadWalker) >= 1.0
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::V0) >= 0.000121
Requires:       perl(Devel::Cycle)
Requires:       perl(PadWalker) >= 1.0
Requires:       perl(Test2::API) >= 1.302015
Provides:       perl(Test2::Tools::MemoryCycle)
%{perl_requires}

%description
Perl's garbage collection has one big problem: Circular references can't
get cleaned up. The above example is the sort of thing that sometimes trips
me up, where a code reference inside a data structure refers to another
part of the data structure. There already exists a good testing module to
find these sort of problems: Test::Memory::Cycle, so why write this one?
Well that module uses Test::Builder, and this one instead uses Test2::API.
If you want to write Test2::Suite tests without pulling in Test::Builder
then this is the cycle testing module for you.

This module also uses the standard Exporter interface, instead of letting
you specify a test plan. That behavior was once in vogue I guess, but I do
not care for it.

%prep
%autosetup  -n %{cpan_name}-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
