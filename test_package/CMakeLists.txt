project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if(UNIX)
  add_executable(example example.cpp)
  target_link_libraries(example ${CONAN_LIBS})

  add_test(NAME ${CMAKE_PROJECT_NAME}
           WORKING_DIRECTORY ${PROJECT_BINARY_DIR}/bin
           COMMAND ${CMAKE_PROJECT_NAME})

elseif(${CMAKE_SYSTEM_NAME} STREQUAL Arduino)

  generate_arduino_firmware(${CMAKE_PROJECT_NAME} SKETCH example.cpp
                            # ARDLIBS StandardCplusplus
                            )
endif()
