# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dota_gcmessages_client_watch.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import dota2.protobufs.dota_gcmessages_common_pb2 as dota__gcmessages__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"dota_gcmessages_client_watch.proto\x12\x04\x64ota\x1a\x1c\x64ota_gcmessages_common.proto\"\xec\x06\n\x12\x43SourceTVGameSmall\x12\x15\n\ractivate_time\x18\x01 \x01(\r\x12\x17\n\x0f\x64\x65\x61\x63tivate_time\x18\x02 \x01(\r\x12\x17\n\x0fserver_steam_id\x18\x03 \x01(\x04\x12\x10\n\x08lobby_id\x18\x04 \x01(\x04\x12\x11\n\tleague_id\x18\x05 \x01(\r\x12\x12\n\nlobby_type\x18\x06 \x01(\r\x12\x11\n\tgame_time\x18\x07 \x01(\x05\x12\r\n\x05\x64\x65lay\x18\x08 \x01(\r\x12\x12\n\nspectators\x18\t \x01(\r\x12\x11\n\tgame_mode\x18\n \x01(\r\x12\x13\n\x0b\x61verage_mmr\x18\x0b \x01(\r\x12\x10\n\x08match_id\x18\x0c \x01(\x04\x12\x11\n\tseries_id\x18\r \x01(\r\x12\x19\n\x11team_name_radiant\x18\x0f \x01(\t\x12\x16\n\x0eteam_name_dire\x18\x10 \x01(\t\x12\x19\n\x11team_logo_radiant\x18\x18 \x01(\x06\x12\x16\n\x0eteam_logo_dire\x18\x19 \x01(\x06\x12\x17\n\x0fteam_id_radiant\x18\x1e \x01(\r\x12\x14\n\x0cteam_id_dire\x18\x1f \x01(\r\x12\x12\n\nsort_score\x18\x11 \x01(\r\x12\x18\n\x10last_update_time\x18\x12 \x01(\x02\x12\x14\n\x0cradiant_lead\x18\x13 \x01(\x05\x12\x15\n\rradiant_score\x18\x14 \x01(\r\x12\x12\n\ndire_score\x18\x15 \x01(\r\x12\x30\n\x07players\x18\x16 \x03(\x0b\x32\x1f.dota.CSourceTVGameSmall.Player\x12\x16\n\x0e\x62uilding_state\x18\x17 \x01(\x07\x12%\n\x1dweekend_tourney_tournament_id\x18\x1a \x01(\r\x12 \n\x18weekend_tourney_division\x18\x1b \x01(\r\x12#\n\x1bweekend_tourney_skill_level\x18\x1c \x01(\r\x12%\n\x1dweekend_tourney_bracket_round\x18\x1d \x01(\r\x12\x1e\n\x16\x63ustom_game_difficulty\x18  \x01(\r\x1aN\n\x06Player\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x0f\n\x07hero_id\x18\x02 \x01(\r\x12\x11\n\tteam_slot\x18\x03 \x01(\r\x12\x0c\n\x04team\x18\x04 \x01(\r\"\x9c\x01\n\"CMsgClientToGCFindTopSourceTVGames\x12\x12\n\nsearch_key\x18\x01 \x01(\t\x12\x11\n\tleague_id\x18\x02 \x01(\r\x12\x0f\n\x07hero_id\x18\x03 \x01(\r\x12\x12\n\nstart_game\x18\x04 \x01(\r\x12\x17\n\x0fgame_list_index\x18\x05 \x01(\r\x12\x11\n\tlobby_ids\x18\x06 \x03(\x04\"\x95\x02\n*CMsgGCToClientFindTopSourceTVGamesResponse\x12\x12\n\nsearch_key\x18\x01 \x01(\t\x12\x11\n\tleague_id\x18\x02 \x01(\r\x12\x0f\n\x07hero_id\x18\x03 \x01(\r\x12\x12\n\nstart_game\x18\x04 \x01(\r\x12\x11\n\tnum_games\x18\x05 \x01(\r\x12\x17\n\x0fgame_list_index\x18\x06 \x01(\r\x12+\n\tgame_list\x18\x07 \x03(\x0b\x32\x18.dota.CSourceTVGameSmall\x12\x16\n\x0especific_games\x18\x08 \x01(\x08\x12*\n\x08\x62ot_game\x18\t \x01(\x0b\x32\x18.dota.CSourceTVGameSmall\"T\n$CMsgGCToClientTopWeekendTourneyGames\x12,\n\nlive_games\x18\x01 \x03(\x0b\x32\x18.dota.CSourceTVGameSmall\"\'\n%CMsgClientToGCTopLeagueMatchesRequest\"\'\n%CMsgClientToGCTopFriendMatchesRequest\"8\n#CMsgClientToGCMatchesMinimalRequest\x12\x11\n\tmatch_ids\x18\x01 \x03(\x04\"g\n$CMsgClientToGCMatchesMinimalResponse\x12+\n\x07matches\x18\x01 \x03(\x0b\x32\x1a.dota.CMsgDOTAMatchMinimal\x12\x12\n\nlast_match\x18\x02 \x01(\x08\"U\n&CMsgGCToClientTopLeagueMatchesResponse\x12+\n\x07matches\x18\x02 \x03(\x0b\x32\x1a.dota.CMsgDOTAMatchMinimal\"U\n&CMsgGCToClientTopFriendMatchesResponse\x12+\n\x07matches\x18\x01 \x03(\x0b\x32\x1a.dota.CMsgDOTAMatchMinimal\"8\n\x16\x43MsgSpectateFriendGame\x12\x10\n\x08steam_id\x18\x01 \x01(\x06\x12\x0c\n\x04live\x18\x02 \x01(\x08\"\xbd\x04\n\x1e\x43MsgSpectateFriendGameResponse\x12\x16\n\x0eserver_steamid\x18\x04 \x01(\x06\x12Y\n\x11watch_live_result\x18\x05 \x01(\x0e\x32\x35.dota.CMsgSpectateFriendGameResponse.EWatchLiveResult:\x07SUCCESS\"\xa7\x03\n\x10\x45WatchLiveResult\x12\x0b\n\x07SUCCESS\x10\x00\x12\x11\n\rERROR_GENERIC\x10\x01\x12\x11\n\rERROR_NO_PLUS\x10\x02\x12\x15\n\x11\x45RROR_NOT_FRIENDS\x10\x03\x12\x19\n\x15\x45RROR_LOBBY_NOT_FOUND\x10\x04\x12\x1e\n\x1a\x45RROR_SPECTATOR_IN_A_LOBBY\x10\x05\x12\x16\n\x12\x45RROR_LOBBY_IS_LAN\x10\x06\x12\x1a\n\x16\x45RROR_WRONG_LOBBY_TYPE\x10\x07\x12\x1b\n\x17\x45RROR_WRONG_LOBBY_STATE\x10\x08\x12\x1b\n\x17\x45RROR_PLAYER_NOT_PLAYER\x10\t\x12\x1d\n\x19\x45RROR_TOO_MANY_SPECTATORS\x10\n\x12\"\n\x1e\x45RROR_SPECTATOR_SWITCHED_TEAMS\x10\x0b\x12\x1f\n\x1b\x45RROR_FRIENDS_ON_BOTH_SIDES\x10\x0c\x12!\n\x1d\x45RROR_SPECTATOR_IN_THIS_LOBBY\x10\r\x12\x19\n\x15\x45RROR_LOBBY_IS_LEAGUE\x10\x0e\"\xd1\x01\n\x17\x43\x44OTAReplayDownloadInfo\x12)\n\x05match\x18\x01 \x01(\x0b\x32\x1a.dota.CMsgDOTAMatchMinimal\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\r\x12\x0c\n\x04tags\x18\x05 \x03(\t\x12\x16\n\x0e\x65xists_on_disk\x18\x06 \x01(\x08\x1a\x33\n\tHighlight\x12\x11\n\ttimestamp\x18\x01 \x01(\r\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x80\x01\n\rCMsgWatchGame\x12\x16\n\x0eserver_steamid\x18\x01 \x01(\x06\x12\x16\n\x0e\x63lient_version\x18\x02 \x01(\r\x12\x1c\n\x14watch_server_steamid\x18\x03 \x01(\x06\x12\x10\n\x08lobby_id\x18\x04 \x01(\x04\x12\x0f\n\x07regions\x18\x05 \x03(\r\"\x15\n\x13\x43MsgCancelWatchGame\"\xce\x03\n\x15\x43MsgWatchGameResponse\x12O\n\x11watch_game_result\x18\x01 \x01(\x0e\x32+.dota.CMsgWatchGameResponse.WatchGameResult:\x07PENDING\x12\x1d\n\x15source_tv_public_addr\x18\x02 \x01(\r\x12\x1e\n\x16source_tv_private_addr\x18\x03 \x01(\r\x12\x16\n\x0esource_tv_port\x18\x04 \x01(\r\x12\x1b\n\x13game_server_steamid\x18\x05 \x01(\x06\x12\x1c\n\x14watch_server_steamid\x18\x06 \x01(\x06\x12#\n\x1bwatch_tv_unique_secret_code\x18\x07 \x01(\x06\"\xac\x01\n\x0fWatchGameResult\x12\x0b\n\x07PENDING\x10\x00\x12\t\n\x05READY\x10\x01\x12\x16\n\x12GAMESERVERNOTFOUND\x10\x02\x12\x0f\n\x0bUNAVAILABLE\x10\x03\x12\r\n\tCANCELLED\x10\x04\x12\x17\n\x13INCOMPATIBLEVERSION\x10\x05\x12\x1d\n\x19MISSINGLEAGUESUBSCRIPTION\x10\x06\x12\x11\n\rLOBBYNOTFOUND\x10\x07\"=\n\x1e\x43MsgPartyLeaderWatchGamePrompt\x12\x1b\n\x13game_server_steamid\x18\x05 \x01(\x06\"\xff\x01\n\x14\x43\x44OTABroadcasterInfo\x12\x12\n\naccount_id\x18\x01 \x01(\r\x12\x17\n\x0fserver_steam_id\x18\x02 \x01(\x06\x12\x0c\n\x04live\x18\x03 \x01(\x08\x12\x19\n\x11team_name_radiant\x18\x04 \x01(\t\x12\x16\n\x0eteam_name_dire\x18\x05 \x01(\t\x12\x13\n\x0bseries_game\x18\x07 \x01(\r\x12$\n\x1cupcoming_broadcast_timestamp\x18\t \x01(\r\x12\x18\n\x10\x61llow_live_video\x18\n \x01(\x08\x12\x11\n\tnode_type\x18\x0b \x01(\r\x12\x11\n\tnode_name\x18\x0c \x01(\t\"\x99\x04\n\x0e\x43MsgDOTASeries\x12\x11\n\tseries_id\x18\x01 \x01(\r\x12\x13\n\x0bseries_type\x18\x02 \x01(\r\x12-\n\x06team_1\x18\x03 \x01(\x0b\x32\x1d.dota.CMsgDOTASeries.TeamInfo\x12-\n\x06team_2\x18\x04 \x01(\x0b\x32\x1d.dota.CMsgDOTASeries.TeamInfo\x12\x31\n\rmatch_minimal\x18\x05 \x03(\x0b\x32\x1a.dota.CMsgDOTAMatchMinimal\x12\x30\n\tlive_game\x18\x06 \x01(\x0b\x32\x1d.dota.CMsgDOTASeries.LiveGame\x1aZ\n\x08TeamInfo\x12\x0f\n\x07team_id\x18\x01 \x01(\r\x12\x11\n\tteam_name\x18\x02 \x01(\t\x12\x15\n\rteam_logo_url\x18\x03 \x01(\t\x12\x13\n\x0bwager_count\x18\x04 \x01(\r\x1a\xbf\x01\n\x08LiveGame\x12\x17\n\x0fserver_steam_id\x18\x01 \x01(\x06\x12\x33\n\x0cteam_radiant\x18\x02 \x01(\x0b\x32\x1d.dota.CMsgDOTASeries.TeamInfo\x12\x30\n\tteam_dire\x18\x03 \x01(\x0b\x32\x1d.dota.CMsgDOTASeries.TeamInfo\x12\x1a\n\x12team_radiant_score\x18\x04 \x01(\r\x12\x17\n\x0fteam_dire_score\x18\x05 \x01(\r')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dota_gcmessages_client_watch_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CSOURCETVGAMESMALL._serialized_start=75
  _CSOURCETVGAMESMALL._serialized_end=951
  _CSOURCETVGAMESMALL_PLAYER._serialized_start=873
  _CSOURCETVGAMESMALL_PLAYER._serialized_end=951
  _CMSGCLIENTTOGCFINDTOPSOURCETVGAMES._serialized_start=954
  _CMSGCLIENTTOGCFINDTOPSOURCETVGAMES._serialized_end=1110
  _CMSGGCTOCLIENTFINDTOPSOURCETVGAMESRESPONSE._serialized_start=1113
  _CMSGGCTOCLIENTFINDTOPSOURCETVGAMESRESPONSE._serialized_end=1390
  _CMSGGCTOCLIENTTOPWEEKENDTOURNEYGAMES._serialized_start=1392
  _CMSGGCTOCLIENTTOPWEEKENDTOURNEYGAMES._serialized_end=1476
  _CMSGCLIENTTOGCTOPLEAGUEMATCHESREQUEST._serialized_start=1478
  _CMSGCLIENTTOGCTOPLEAGUEMATCHESREQUEST._serialized_end=1517
  _CMSGCLIENTTOGCTOPFRIENDMATCHESREQUEST._serialized_start=1519
  _CMSGCLIENTTOGCTOPFRIENDMATCHESREQUEST._serialized_end=1558
  _CMSGCLIENTTOGCMATCHESMINIMALREQUEST._serialized_start=1560
  _CMSGCLIENTTOGCMATCHESMINIMALREQUEST._serialized_end=1616
  _CMSGCLIENTTOGCMATCHESMINIMALRESPONSE._serialized_start=1618
  _CMSGCLIENTTOGCMATCHESMINIMALRESPONSE._serialized_end=1721
  _CMSGGCTOCLIENTTOPLEAGUEMATCHESRESPONSE._serialized_start=1723
  _CMSGGCTOCLIENTTOPLEAGUEMATCHESRESPONSE._serialized_end=1808
  _CMSGGCTOCLIENTTOPFRIENDMATCHESRESPONSE._serialized_start=1810
  _CMSGGCTOCLIENTTOPFRIENDMATCHESRESPONSE._serialized_end=1895
  _CMSGSPECTATEFRIENDGAME._serialized_start=1897
  _CMSGSPECTATEFRIENDGAME._serialized_end=1953
  _CMSGSPECTATEFRIENDGAMERESPONSE._serialized_start=1956
  _CMSGSPECTATEFRIENDGAMERESPONSE._serialized_end=2529
  _CMSGSPECTATEFRIENDGAMERESPONSE_EWATCHLIVERESULT._serialized_start=2106
  _CMSGSPECTATEFRIENDGAMERESPONSE_EWATCHLIVERESULT._serialized_end=2529
  _CDOTAREPLAYDOWNLOADINFO._serialized_start=2532
  _CDOTAREPLAYDOWNLOADINFO._serialized_end=2741
  _CDOTAREPLAYDOWNLOADINFO_HIGHLIGHT._serialized_start=2690
  _CDOTAREPLAYDOWNLOADINFO_HIGHLIGHT._serialized_end=2741
  _CMSGWATCHGAME._serialized_start=2744
  _CMSGWATCHGAME._serialized_end=2872
  _CMSGCANCELWATCHGAME._serialized_start=2874
  _CMSGCANCELWATCHGAME._serialized_end=2895
  _CMSGWATCHGAMERESPONSE._serialized_start=2898
  _CMSGWATCHGAMERESPONSE._serialized_end=3360
  _CMSGWATCHGAMERESPONSE_WATCHGAMERESULT._serialized_start=3188
  _CMSGWATCHGAMERESPONSE_WATCHGAMERESULT._serialized_end=3360
  _CMSGPARTYLEADERWATCHGAMEPROMPT._serialized_start=3362
  _CMSGPARTYLEADERWATCHGAMEPROMPT._serialized_end=3423
  _CDOTABROADCASTERINFO._serialized_start=3426
  _CDOTABROADCASTERINFO._serialized_end=3681
  _CMSGDOTASERIES._serialized_start=3684
  _CMSGDOTASERIES._serialized_end=4221
  _CMSGDOTASERIES_TEAMINFO._serialized_start=3937
  _CMSGDOTASERIES_TEAMINFO._serialized_end=4027
  _CMSGDOTASERIES_LIVEGAME._serialized_start=4030
  _CMSGDOTASERIES_LIVEGAME._serialized_end=4221
# @@protoc_insertion_point(module_scope)
