# -*- coding: utf-8 -*-
DUP_NAME = 'Dups'
SUBSTRING_NAME = 'Substr'
GRAPH_TYPES = [DUP_NAME, SUBSTRING_NAME]
AMBIG_NAME = 'Ambig'
SHORT_NAME = 'Short'
FILESMALL_NAME = 'Small'
NUMBER_TYPES = [AMBIG_NAME, SHORT_NAME, FILESMALL_NAME]
STRING_TYPES = ['Name']
LENGTH_NAME = 'Length'
SEQS_NAME = 'Seqs'
LOG_TYPES = [LENGTH_NAME, SEQS_NAME]
STAT_TYPES = NUMBER_TYPES + LOG_TYPES
STAT_COLS = STRING_TYPES + ['SeqsIn', SEQS_NAME, 'Resids'] + NUMBER_TYPES + GRAPH_TYPES
