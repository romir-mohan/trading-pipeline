file(GLOB INTERN_PROJECT_MAIN src/cppsrc/main.cpp)
file(GLOB_RECURSE INTERN_PROJECT_HEADERS src/cppsrc/*.hpp)
file(GLOB_RECURSE INTERN_PROJECT_TESTS src/cppsrc/test/*.cpp)

add_executable(intern_project ${INTERN_PROJECT_MAIN} ${INTERN_PROJECT_HEADERS})

add_executable(intern_tests ${INTERN_PROJECT_TESTS} ${INTERN_PROJECT_HEADERS})
target_include_directories(intern_tests PUBLIC src)

target_link_libraries(intern_project PRIVATE Python3::Python)
target_link_libraries(intern_project PRIVATE pybind11::pybind11)
target_link_libraries(intern_project PRIVATE ${Python3_LIBRARIES})
target_link_libraries(intern_project PRIVATE cpr::cpr)
target_link_libraries(intern_project PRIVATE nlohmann_json::nlohmann_json)

target_link_libraries(intern_tests PRIVATE Python3::Python)
target_link_libraries(intern_tests PRIVATE pybind11::pybind11)
target_link_libraries(intern_tests PRIVATE ${Python3_LIBRARIES})
target_link_libraries(intern_tests PRIVATE gtest::gtest)
target_link_libraries(intern_tests PRIVATE cpr::cpr)
target_link_libraries(intern_tests PRIVATE nlohmann_json::nlohmann_json)

pybind11_add_module(intern src/cppsrc/main.cpp)
target_link_libraries(intern PRIVATE cpr::cpr)
target_link_libraries(intern PRIVATE nlohmann_json::nlohmann_json)

install(TARGETS intern DESTINATION intern_project)