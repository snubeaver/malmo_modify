from __future__ import print_function
# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

from builtins import range
import MalmoPython
import os
import random
import sys
import time
import json
import errno
import malmoutils
from PIL import Image

malmoutils.fix_print()

agent_host = MalmoPython.AgentHost()
agent_host.addOptionalIntArgument( "speed,s", "Length of tick, in ms.", 50)
malmoutils.parse_command_line(agent_host)

maze1 = '''
    <MazeDecorator>
        <SizeAndPosition length="60" width="60" yOrigin="225" zOrigin="0" height="180"/>
        <GapProbability variance="0.4">0.5</GapProbability>
        <Seed>random</Seed>
        <MaterialSeed>random</MaterialSeed>
        <AllowDiagonalMovement>false</AllowDiagonalMovement>
        <StartBlock fixedToEdge="true" type="emerald_block" height="1"/>
        <EndBlock fixedToEdge="true" type="redstone_block diamond_block gold_block" height="12"/>
        <PathBlock type="stained_hardened_clay" colour="WHITE ORANGE MAGENTA LIGHT_BLUE YELLOW LIME PINK GRAY SILVER CYAN PURPLE BLUE BROWN GREEN RED BLACK" height="1"/>
        <FloorBlock type="stone"/>
        <GapBlock type="air"/>
        <AddQuitProducer description="finished maze"/>
        <AddNavigationObservations/>
    </MazeDecorator>
'''

maze2 = '''
    <MazeDecorator>
        <SizeAndPosition length="20" width="20" scale="2" yOrigin="225" zOrigin="0" height="180"/>
        <GapProbability variance="0.4">0.5</GapProbability>
        <Seed>random</Seed>
        <MaterialSeed>random</MaterialSeed>
        <AllowDiagonalMovement>false</AllowDiagonalMovement>
        <StartBlock fixedToEdge="true" type="emerald_block" height="1"/>
        <EndBlock fixedToEdge="true" type="redstone_block lapis_block" height="12"/>
        <PathBlock type="stained_glass" colour="WHITE ORANGE MAGENTA LIGHT_BLUE YELLOW LIME PINK GRAY SILVER CYAN PURPLE BLUE BROWN GREEN RED BLACK" height="1"/>
        <FloorBlock type="glowstone"/>
        <Waypoints quantity="30">
            <WaypointBlock type= "grass"/>
        </Waypoints>
        <GapBlock type="stone" height="2"/>
        <AddQuitProducer description="finished maze"/>
        <AddNavigationObservations/>
    </MazeDecorator>
    <DrawingDecorator>
        <DrawCuboid type="cobblestone" x1="-1" x2="0" y1="226" y2="276" z1="-1" z2="41"/>
        <DrawCuboid type="cobblestone" x1="40" x2="41" y1="226" y2="276" z1="-1" z2="41"/>
        <DrawCuboid type="cobblestone" x1="-1" x2="41" y1="226" y2="276" z1="-1" z2="0"/>
        <DrawCuboid type="cobblestone" x1="-1" x2="41" y1="226" y2="276" z1="40" z2="41"/>
    </DrawingDecorator>
'''

maze3 = '''
    <MazeDecorator>
        <SizeAndPosition length="60" width="60" yOrigin="225" zOrigin="0" height="180"/>
        <GapProbability>0.2</GapProbability>
        <Seed>random</Seed>
        <MaterialSeed>random</MaterialSeed>
        <AllowDiagonalMovement>false</AllowDiagonalMovement>
        <StartBlock fixedToEdge="true" type="emerald_block" height="1"/>
        <EndBlock fixedToEdge="true" type="redstone_block" height="12"/>
        <PathBlock type="glowstone stained_glass dirt" colour="WHITE ORANGE MAGENTA LIGHT_BLUE YELLOW LIME PINK GRAY SILVER CYAN PURPLE BLUE BROWN GREEN RED BLACK" height="1"/>
        <FloorBlock type="stone" variant="smooth_granite"/>
        <SubgoalBlock type="beacon sea_lantern glowstone"/>
        <GapBlock type="air"/>
        <AddQuitProducer description="finished maze"/>
        <AddNavigationObservations/>
   </MazeDecorator>
'''

maze4 = '''
    <MazeDecorator>
        <SizeAndPosition length="60" width="60" yOrigin="225" zOrigin="0" height="180"/>
        <GapProbability variance="0.4">0.5</GapProbability>
        <Seed>random</Seed>
        <MaterialSeed>random</MaterialSeed>
        <AllowDiagonalMovement>false</AllowDiagonalMovement>
        <StartBlock fixedToEdge="true" type="emerald_block" height="1"/>
        <EndBlock fixedToEdge="true" type="redstone_block" height="12"/>
        <PathBlock type="stone dirt stained_hardened_clay" colour="WHITE ORANGE MAGENTA LIGHT_BLUE YELLOW LIME PINK GRAY SILVER CYAN PURPLE BLUE BROWN GREEN RED BLACK" height="1"/>
        <FloorBlock type="stone" variant="smooth_granite"/>
        <SubgoalBlock type="beacon sea_lantern glowstone"/>
        <OptimalPathBlock type="stone" variant="smooth_granite andesite smooth_diorite diorite"/>
        <GapBlock type="lapis_ore stained_hardened_clay air" colour="WHITE ORANGE MAGENTA LIGHT_BLUE YELLOW LIME PINK GRAY SILVER CYAN PURPLE BLUE BROWN GREEN RED BLACK" height="3" heightVariance="3"/>
        <AddQuitProducer description="finished maze"/>
        <AddNavigationObservations/>
    </MazeDecorator>
'''

def GetMissionXML( mazeblock, agent_host ):
    return '''<?xml version="1.0" encoding="UTF-8" ?>
    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <About>
            <Summary>Run the maze!</Summary>
        </About>

        <ModSettings>
            <MsPerTick>''' + str(TICK_LENGTH) + '''</MsPerTick>
        </ModSettings>

        <ServerSection>
            <ServerInitialConditions>
                <AllowSpawning>false</AllowSpawning>
            </ServerInitialConditions>
            <ServerHandlers>
                <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1" />
                ''' + mazeblock + '''
                <ServerQuitFromTimeUp timeLimitMs="45000"/>
                <ServerQuitWhenAnyAgentFinishes />
            </ServerHandlers>
        </ServerSection>

        <AgentSection mode="Creative">
            <Name>James Bond</Name>
            <AgentStart>
                <Placement x="-20" y="81" z="21"/>
            </AgentStart>
            <AgentHandlers>
                <ContinuousMovementCommands turnSpeedDegs="840">
                    <ModifierList type="deny-list"> <!-- Example deny-list: prevent agent from strafing -->
                        <command>strafe</command>
                    </ModifierList>
                </ContinuousMovementCommands>''' + malmoutils.get_video_xml(agent_host) + '''
                </AgentHandlers>
        </AgentSection>

    </Mission>'''

validate = True
# mazeblocks = [maze1, maze2, maze3, maze4]
mazeblocks = [maze2]
agent_host.setObservationsPolicy(MalmoPython.ObservationsPolicy.LATEST_OBSERVATION_ONLY)

if agent_host.receivedArgument("test"):
    num_reps = 10
else:
    num_reps = 30000

TICK_LENGTH = agent_host.getIntArgument("speed")

for iRepeat in range(num_reps):
    my_mission_record = malmoutils.get_default_recording_object(agent_host, "Mission_{}".format(iRepeat + 1))
    mazeblock = random.choice(mazeblocks)
    my_mission = MalmoPython.MissionSpec(GetMissionXML(mazeblock, agent_host),validate)

    max_retries = 3
    for retry in range(max_retries):
        try:
            agent_host.startMission( my_mission, my_mission_record )
            break
        except RuntimeError as e:
            if retry == max_retries - 1:
                print("Error starting mission:",e)
                exit(1)
            else:
                time.sleep(2)

    print("Waiting for the mission to start", end=' ')
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        print(".", end="")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        if len(world_state.errors):
            print()
            for error in world_state.errors:
                print("Error:",error.text)
                exit()
    print()

    # main loop:
    while world_state.is_mission_running:
        if world_state.number_of_observations_since_last_state > 0:
            print("Got " + str(world_state.number_of_observations_since_last_state) + " observations since last state.")
            msg = world_state.observations[-1].text
            ob = json.loads(msg)
            current_yaw_delta = ob.get(u'yawDelta', 0) + random.uniform(-0.01,0.01)
            current_speed = (1-abs(current_yaw_delta))
            print("Got observation: " + str(current_yaw_delta))

            try:
                agent_host.sendCommand( "move " + str(current_speed) )
                agent_host.sendCommand( "turn " + str(current_yaw_delta) )
            except RuntimeError as e:
                print("Failed to send command:",e)
                pass

        import sys, time
        sys.stdout.flush()

        world_state = agent_host.getWorldState()
        # ADDED
        num_frames_seen = world_state.number_of_video_frames_since_last_state
        while world_state.is_mission_running and world_state.number_of_video_frames_since_last_state == 0:
            #print(len(world_state.video_frames))
            world_state = agent_host.peekWorldState()
            time.sleep(0.5)
        print("HERE")
        print(len(world_state.video_frames))
        sys.stdout.flush()
        if True:
            # save the frame, for debugging
            if world_state.is_mission_running:
                assert len(world_state.video_frames) > 0, 'No video frames!?'
                frame = world_state.video_frames[-1]
                image = Image.frombytes('RGB', (frame.width, frame.height), bytes(frame.pixels) )
                iFrame = iFrame + 1
                image.save( 'rep_' + str(self.rep).zfill(3) + '_saved_frame_' + str(iFrame).zfill(4) + '.png' )

    print("Mission has stopped.")
    time.sleep(0.5) # Give mod a little time to get back to dormant state.
