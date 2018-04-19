from gym.envs.registration import register

register(
    id='cliff-v0',
    entry_point='gym_cliff.envs:CliffEnv',
)
register(
    id='cliff-extrahard-v0',
    entry_point='gym_cliff.envs:CliffExtraHardEnv',
)
