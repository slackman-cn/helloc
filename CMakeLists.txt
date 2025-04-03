cmake_minimum_required(VERSION 3.10)
project(helloc)

set(CMAKE_C_STANDARD 99)
set(CMAKE_CXX_STANDARD 11)

# 创建静态库
add_library(addnum  STATIC
    src/add_num.cpp
)
target_include_directories(addnum
    PUBLIC
        ${PROJECT_SOURCE_DIR}/include
)

# 主程序
add_executable(helloc
    src/main.cpp
)
target_link_libraries(helloc
    PRIVATE
        addnum
)

install(TARGETS ${PROJECT_NAME}
        RUNTIME DESTINATION "bin" )


############ Create RPM
SET(CPACK_GENERATOR "RPM")
set(CPACK_PACKAGE_VERSION "1.0.0")
set(CPACK_RPM_PACKAGE_RELEASE 1)
set(CPACK_RPM_FILE_NAME "RPM-DEFAULT")
set(CPACK_RPM_PACKAGE_URL "https://local.host")
set(CPACK_RPM_PACKAGE_LICENSE "Apache 2.0 + Common Clause 1.0")
set(CPACK_RPM_PACKAGE_SUMMARY "Hello cpp from Linux")
set(CPACK_RPM_PACKAGE_DESCRIPTION "Hello cpp from Linux")
set(CPACK_RPM_PACKAGE_GROUP "Applications/Text")

set(CPACK_PACKAGE_CONTACT "slackman@disroot.org")
set(CPACK_PACKAGE_VENDOR "slackman-cn")

set(CPACK_RPM_PACKAGE_AUTOREQ "NO")
set(CPACK_RPM_PACKAGE_AUTOPROV "NO")
set(CPACK_RPM_DEFAULT_FILE_PERMISSIONS
        OWNER_READ OWNER_EXECUTE OWNER_WRITE
        GROUP_READ GROUP_EXECUTE
        WORLD_READ WORLD_EXECUTE )
set(CPACK_PACKAGING_INSTALL_PREFIX "/opt/helloc")
include(CPack)
