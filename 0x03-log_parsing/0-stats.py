#!/usr/bin/python3
'''
A script for parsing HTTP request logs.
'''

import re
from typing import Dict, Optional


def parse_log_line(request_line: str) -> Optional[Dict[str, int]]:
    '''Extracts sections of a line of an HTTP request log.

    Args:
        request_line (str): The line of the HTTP request log.

    Returns:
        dict: A dictionary containing extracted information or None
        if the line format is invalid.
    '''
    field_patterns = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info: Dict[str, int] = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(*field_patterns)
    response_match = re.fullmatch(log_format, request_line)
    if response_match is not None:
        status_code = response_match.group('status_code')
        file_size = int(response_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_processed_size: int,
                     status_code_counts: Dict[str, int]) -> None:
    '''Prints the accumulated statistics of the HTTP request log.

    Args:
        total_processed_size (int): The total size of processed files.
        status_code_counts (dict): A dictionary containing counts
        for each status code.
    '''
    print('File size: {:d}'.format(total_processed_size), flush=True)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts.get(status_code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count), flush=True)


def update_metrics(line: str, total_processed_size: int,
                   status_code_counts: Dict[str, int]) -> int:
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_processed_size (int): The current total file size.
        status_code_counts (dict): A dictionary containing counts
        for each status code.

    Returns:
        int: The new total file size.
    '''
    extracted_log_info = parse_log_line(line)
    if not extracted_log_info:
        return total_processed_size
    status_code = extracted_log_info.get('status_code', '0')
    if status_code in status_code_counts.keys():
        status_code_counts[status_code] += 1
    return total_processed_size + extracted_log_info['file_size']


def main() -> None:
    '''Starts the log parser.
    '''
    line_number = 0
    total_processed_size = 0
    status_code_counts: Dict[str, int] = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_processed_size = update_metrics(
                line,
                total_processed_size,
                status_code_counts,
            )
            line_number += 1
            if line_number % 10 == 0:
                print_statistics(total_processed_size, status_code_counts)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_processed_size, status_code_counts)


if __name__ == '__main__':
    main()
