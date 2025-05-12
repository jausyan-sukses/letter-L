from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch MAVROS untuk konek ke Flight Controller
        Node(
            package='mavros',
            executable='mavros_node',
            name='mavros',
            output='screen',
            parameters=[{
                'fcu_url': '/dev/ttyACM0:57600',  # port USB ke MiniPix
                'gcs_url': '',
                'target_system_id': 1,
                'target_component_id': 1,
                'system_id': 1,
                'component_id': 1,
            }]
        ),
        
        # Launch Teleop kamu
        Node(
            package='drone_teleop',
            executable='drone_teleop',  # Nama executable hasil compile dari CMakeLists
            name='drone_teleop',
            output='screen'
        )
    ])
