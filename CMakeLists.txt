cmake_minimum_required(VERSION 3.5)

set(PROJECT_NAME BOLIDE_Player)
project(${PROJECT_NAME})
enable_testing()

set(CONAN_BUILD_INFO_FILE ${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
if(NOT EXISTS ${CONAN_BUILD_INFO_FILE})
  message(
    WARNING
      "The file conanbuildinfo.cmake doesn't exist.\nRunning 'conan install' first..."
    )
  execute_process(COMMAND conan install "${CMAKE_CURRENT_SOURCE_DIR}"
                          -if="${CMAKE_CURRENT_BINARY_DIR}")
endif()

include(${CONAN_BUILD_INFO_FILE})
conan_basic_setup()

file(GLOB_RECURSE ALL_HDRS src/*.h)
file(GLOB_RECURSE ALL_SRCS src/*.cpp)


if(UNIX)
  add_library(${PROJECT_NAME} STATIC ${ALL_HDRS} ${ALL_SRCS})
elseif(${CMAKE_SYSTEM_NAME} STREQUAL Arduino)
  generate_arduino_library(${PROJECT_NAME})
endif()
