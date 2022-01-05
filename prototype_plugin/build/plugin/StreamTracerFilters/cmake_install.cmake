# Install script for directory: /Users/jan/Google Drive/Programmieren/bachelor_thesis/prototype_plugin/plugin/StreamTracerFilters

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/Library/Developer/CommandLineTools/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelopmentx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES
    "/Users/jan/Google Drive/Programmieren/bachelor_thesis/prototype_plugin/plugin/StreamTracerFilters/vtkMyStreamTracerFilter.h"
    "/Users/jan/Google Drive/Programmieren/bachelor_thesis/prototype_plugin/build/plugin/StreamTracerFilters/StreamTracerFiltersModule.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelopmentx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/StreamTracerFilter/vtk/hierarchy/StreamTracerFilter" TYPE FILE RENAME "StreamTracerFilters-hierarchy.txt" FILES "/Users/jan/Google Drive/Programmieren/bachelor_thesis/prototype_plugin/build/lib/StreamTracerFilter/vtk/hierarchy/StreamTracerFilter/StreamTracerFilters-hierarchy.txt")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xruntimex" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/StreamTracerFilter" TYPE SHARED_LIBRARY FILES "/Users/jan/Google Drive/Programmieren/bachelor_thesis/prototype_plugin/build/lib/StreamTracerFilter/libStreamTracerFilters.dylib")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/StreamTracerFilter/libStreamTracerFilters.dylib" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/StreamTracerFilter/libStreamTracerFilters.dylib")
    execute_process(COMMAND "/usr/bin/install_name_tool"
      -id "@loader_path/libStreamTracerFilters.dylib"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/StreamTracerFilter/libStreamTracerFilters.dylib")
    execute_process(COMMAND /usr/bin/install_name_tool
      -delete_rpath "/Applications/ParaView/lib"
      -add_rpath "@loader_path"
      -add_rpath "@loader_path/../"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/StreamTracerFilter/libStreamTracerFilters.dylib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Library/Developer/CommandLineTools/usr/bin/strip" -x "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/StreamTracerFilter/libStreamTracerFilters.dylib")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelopmentx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()
