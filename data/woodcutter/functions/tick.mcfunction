# Increment global timers by 1
scoreboard players add wc_timer_player wc_internals 1


# If player timer exceeds m_player_interval, call the function it's supposed to run (and reset it back to 0)
execute if score wc_timer_player wc_internals >= wc_checker_interval wc_options run function woodcutter:on_player_interval

