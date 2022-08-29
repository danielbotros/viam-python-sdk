import asyncio
import logging

from viam.proto.api.common import GeoPoint, Orientation, Vector3
from viam.rpc.server import Server

from .components import (
    ExampleAnalogReader,
    ExampleArm,
    ExampleBase,
    ExampleBoard,
    ExampleCamera,
    ExampleDigitalInterrupt,
    ExampleGantry,
    ExampleGPIOPin,
    ExampleGripper,
    ExampleMotor,
    ExampleMovementSensor,
    ExamplePoseTracker,
    ExampleSensor,
    ExampleServo,
    MovementSensor,
)


async def run():
    my_arm = ExampleArm("arm0")
    my_base = ExampleBase("base0")
    my_board = ExampleBoard(
        name="board",
        analog_readers={
            "reader1": ExampleAnalogReader("reader1", 3),
        },
        digital_interrupts={
            "interrupt1": ExampleDigitalInterrupt("interrupt1"),
        },
        gpio_pins={
            "pin1": ExampleGPIOPin("pin1"),
        },
    )
    my_camera = ExampleCamera("camera0")
    my_gantry = ExampleGantry("gantry0", [1, 2, 3], [4, 5, 6])
    my_gripper = ExampleGripper("gripper0")
    my_motor = ExampleMotor("motor0")
    my_movement_sensor = ExampleMovementSensor(
        "movement_sensor0",
        GeoPoint(latitude=40.664679865782624, longitude=-73.97668056188789),
        15,
        Vector3(x=1, y=2, z=3),
        Vector3(x=1, y=2, z=3),
        182,
        Orientation(o_x=1, o_y=2, o_z=3, theta=5),
        MovementSensor.Properties(
            linear_velocity_supported=False,
            angular_velocity_supported=True,
            orientation_supported=False,
            position_supported=True,
            compass_heading_supported=False,
        ),
        {"foo": 0.1, "bar": 2.0, "baz": 3.14},
    )
    my_pose_tracker = ExamplePoseTracker("pose_tracker0")
    my_sensor = ExampleSensor("sensor0")
    my_servo = ExampleServo("servo0")
    server = Server(
        components=[
            my_arm,
            my_base,
            my_board,
            my_camera,
            my_gantry,
            my_gripper,
            my_motor,
            my_movement_sensor,
            my_pose_tracker,
            my_sensor,
            my_servo,
        ]
    )
    await server.serve(host="0.0.0.0", port=5000, log_level=logging.DEBUG)


if __name__ == "__main__":
    asyncio.run(run())
