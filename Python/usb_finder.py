"""Contain usb_finder."""

import serial.tools.list_ports  # pip install pyserial


def _get_hw_vendor(hwid):
    """Extract the vendor ID from the hardware id."""
    return  hwid.split(' ')[1].split('=')[1].split(':')[0]


def usb_finder(vendor_id, logging=None):
    """
    Identify the connection type for all serial connections.

    Args:
        vendor_id: The vendor ID of the hardware device wanted.
        logging: (optional) The python logging function.
                 default None, no logging.

    Returns:
        The port location, as string,
        None if not found.
    """
    ports = serial.tools.list_ports.comports()
    for port_no, desc, hwid in ports:
        if logging:
            logging.info("link: {} - description: {}".format(port_no,
                                                             desc))
            logging.debug("address: {}".format(hwid))
        if _get_hw_vendor(hwid) == vendor_id:
            return port_no
    return None
