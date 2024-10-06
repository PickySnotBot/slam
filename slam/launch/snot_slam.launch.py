import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

# Path to the configuration files
pkg_share = get_package_share_directory('slam')
slam_config_file = PathJoinSubstitution([pkg_share, 'config', 'snot_mapper_params_online_async.yaml'])

def generate_launch_description():
    return LaunchDescription([
        # Set console output formatting and colorization
        SetEnvironmentVariable(name='RCUTILS_CONSOLE_OUTPUT_FORMAT', value=["[{time}]: [{severity}] [{name}]: {message}"]),
        SetEnvironmentVariable(name='RCUTILS_COLORIZED_OUTPUT', value=['1']),

        # Declare launch arguments
        DeclareLaunchArgument(
            'use_sim_time', default_value='false',
            description='Use simulation clock if true'),

        # SLAM Node
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[slam_config_file, {'use_sim_time': LaunchConfiguration('use_sim_time')}],
            respawn=True
        )
    ])
