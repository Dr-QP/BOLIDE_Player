cmake_minimum_required(VERSION 3.5)

set(PROJECT_NAME BOLIDE_Player)
project(${PROJECT_NAME})

if(NOT EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    # message(ERROR "The file conanbuildinfo.cmake doesn't exist.\nPlease run 'conan install' first")
    execute_process(COMMAND conan install "${CMAKE_CURRENT_SOURCE_DIR}" WORKING_DIRECTORY ${CMAKE_BINARY_DIR})
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB_RECURSE ALL_HDRS ${CMAKE_CURRENT_SOURCE_DIR}/*.h)
file(GLOB_RECURSE ALL_SRCS ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)

add_library(${PROJECT_NAME} STATIC ${ALL_HDRS} ${ALL_SRCS})

