# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-jsonschema-specifications
Epoch: 100
Version: 2023.12.1
Release: 1%{?dist}
BuildArch: noarch
Summary: The JSON Schema meta-schemas and vocabularies, exposed as a Registry
License: MIT
URL: https://github.com/python-jsonschema/jsonschema-specifications/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
JSON support files from the JSON Schema Specifications (metaschemas,
vocabularies, etc.), packaged for runtime access from Python as a
referencing-based Schema Registry.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-jsonschema-specifications
Summary: The JSON Schema meta-schemas and vocabularies, exposed as a Registry
Requires: python3
Requires: python3-importlib-resources >= 1.4.0
Requires: python3-referencing >= 0.31.0
Provides: python3-jsonschema-specifications = %{epoch}:%{version}-%{release}
Provides: python3dist(jsonschema-specifications) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jsonschema-specifications = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jsonschema-specifications) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jsonschema-specifications = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jsonschema-specifications) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-jsonschema-specifications
JSON support files from the JSON Schema Specifications (metaschemas,
vocabularies, etc.), packaged for runtime access from Python as a
referencing-based Schema Registry.

%files -n python%{python3_version_nodots}-jsonschema-specifications
%license COPYING
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-jsonschema-specifications
Summary: The JSON Schema meta-schemas and vocabularies, exposed as a Registry
Requires: python3
Requires: python3-importlib-resources >= 1.4.0
Requires: python3-referencing >= 0.31.0
Provides: python3-jsonschema-specifications = %{epoch}:%{version}-%{release}
Provides: python3dist(jsonschema-specifications) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jsonschema-specifications = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jsonschema-specifications) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jsonschema-specifications = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jsonschema-specifications) = %{epoch}:%{version}-%{release}

%description -n python3-jsonschema-specifications
JSON support files from the JSON Schema Specifications (metaschemas,
vocabularies, etc.), packaged for runtime access from Python as a
referencing-based Schema Registry.

%files -n python3-jsonschema-specifications
%license COPYING
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-jsonschema-specifications
Summary: The JSON Schema meta-schemas and vocabularies, exposed as a Registry
Requires: python3
Requires: python3-importlib-resources >= 1.4.0
Requires: python3-referencing >= 0.31.0
Provides: python3-jsonschema-specifications = %{epoch}:%{version}-%{release}
Provides: python3dist(jsonschema-specifications) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-jsonschema-specifications = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(jsonschema-specifications) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-jsonschema-specifications = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(jsonschema-specifications) = %{epoch}:%{version}-%{release}

%description -n python3-jsonschema-specifications
JSON support files from the JSON Schema Specifications (metaschemas,
vocabularies, etc.), packaged for runtime access from Python as a
referencing-based Schema Registry.

%files -n python3-jsonschema-specifications
%license COPYING
%{python3_sitelib}/*
%endif

%changelog
