from tools import  *
from objects import *
from routines import *


# ExampleBot2 is a more complex example to showcase how to put routines to use!

class ExampleBot(GoslingAgent):
    def run(agent):
        # This is just some code to warn us if we're offsides
        ball_dist_to_owngoal = (agent.ball.location - agent.friend_goal.location).magnitude()
        my_dist_to_owngoal = (agent.me.location - agent.friend_goal.location).magnitude()
        ball_closer_than_me = ball_dist_to_owngoal < my_dist_to_owngoal

        left_test_a, left_test_b = Vector3(-4100 * side(agent.team), agent.ball.location.y, 0), Vector3(4100 * side(agent.team), agent.ball.location.y, 0)
        agent.line(agent.me.location, left_test_a, (0, 255, 0))
        agent.line(agent.me.location, left_test_b, (255, 0, 0))

        # Create color objects
        white = agent.renderer.create_color(255, 255, 255, 255)
        cyan = agent.renderer.create_color(0, 255, 255, 255)

        # Draw state information
        agent.renderer.draw_string_2d(20, 20, 2, 2, f"Position: {agent.me.location}", white)
        agent.renderer.draw_string_2d(20, 40, 2, 2, f"Velocity: {agent.me.velocity}", white)

        # Debug print to verify execution
        print("Running bot logic")

        # If the stack currently has routines on it, we won't do anything else.
        if len(agent.stack) < 1:
            if agent.kickoff_flag:
                agent.push(kickoff())
            else:
                targets = {
                    "goal": (agent.foe_goal.left_post, agent.foe_goal.right_post),
                    "clear": (Vector3(-4100 * side(agent.team), agent.ball.location.y, 0), Vector3(4100 * side(agent.team), agent.ball.location.y, 0))
                }

                shots = find_hits(agent, targets)

                if len(shots["goal"]) > 0:
                    def score_shot(x):
                        distance = (x.ball_location - agent.me.location).magnitude()
                        speed = distance / (x.intercept_time - agent.time)
                        return speed * x.ratio

                    best_shot = shots["goal"][0]
                    best_shot_score = score_shot(shots["goal"][0])
                    for shot in shots["goal"]:
                        score = score_shot(shot)
                        if score > best_shot_score:
                            best_shot = shot
                            best_shot_score = score

                    if score_shot(best_shot) > 500:
                        agent.push(best_shot)
                        agent.renderer.draw_line_3d(agent.me.location, best_shot.ball_location, cyan)  # Draw arrow to best shot
                    elif len(shots["clear"]) > 0:
                        agent.push(shots["clear"][0])
                        agent.renderer.draw_line_3d(agent.me.location, shots["clear"][0].ball_location, cyan)  # Draw arrow to clear shot

                elif len(shots["clear"]) > 0:
                    agent.push(shots["clear"][0])
                    agent.renderer.draw_line_3d(agent.me.location, shots["clear"][0].ball_location, cyan)  # Draw arrow to clear shot

                elif agent.me.boost < 30:
                    best_boost = None
                    best_boost_value = -1.0

                    for boost in agent.boosts:
                        if not boost.large: continue
                        if not boost.active: continue

                        me_to_boost = (boost.location - agent.me.location).normalize()
                        boost_to_goal = (agent.friend_goal.location - boost.location).normalize()

                        if boost_to_goal.dot(me_to_boost) > best_boost_value:
                            best_boost_value = boost_to_goal.dot(me_to_boost)
                            best_boost = boost
                    if best_boost is not None:
                        agent.push(goto_boost(best_boost, agent.friend_goal.location))
                        agent.renderer.draw_line_3d(agent.me.location, best_boost.location, cyan)  # Draw arrow to boost

                elif ball_closer_than_me and abs(agent.ball.location.x) < 2000:
                    agent.push(short_shot(agent.foe_goal.location))
                    agent.renderer.draw_line_3d(agent.me.location, agent.foe_goal.location, cyan)  # Draw arrow to foe goal

                if len(agent.stack) < 1:
                    left_dist = (agent.friend_goal.left_post - agent.me.location).magnitude()
                    right_dist = (agent.friend_goal.right_post - agent.me.location).magnitude()
                    if left_dist < right_dist:
                        target = agent.friend_goal.left_post
                    else:
                        target = agent.friend_goal.right_post

                    target_to_car = (agent.me.location - target).normalize()
                    target_to_ball = (agent.ball.location - target)
                    final_dist = target_to_car.dot(target_to_ball) * 0.5

                    target += target_to_car * final_dist

                    best_boost = None
                    best_boost_value = -1.0

                    for boost in agent.boosts:
                        if not boost.active: continue
                        me_to_boost = (boost.location - agent.me.location).normalize()
                        boost_to_target = (target - boost.location).normalize()
                        if boost_to_target.dot(me_to_boost) > best_boost_value:
                            best_boost_value = boost_to_target.dot(me_to_boost)
                            best_boost = boost

                    if best_boost is not None and best_boost_value > 0.7 and agent.me.boost < 100:
                        agent.push(goto_boost(best_boost, target))
                        agent.renderer.draw_line_3d(agent.me.location, best_boost.location, cyan)  # Draw arrow to boost
                    else:
                        relative_target = target - agent.me.location
                        distance = relative_target.magnitude()
                        local_target = agent.me.local(relative_target)
                        defaultPD(agent, local_target)
                        defaultThrottle(agent, cap(distance * 2, 0, 2300))

                        agent.controller.boost = False
                        agent.renderer.draw_line_3d(agent.me.location, target, cyan)  # Draw arrow to target