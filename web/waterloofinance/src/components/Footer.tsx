import React from "react";
import { Box, Flex, Link as ChakraLink, Text } from "@chakra-ui/react";

const Footer = () => {
  return (
    <Box bg="teal" p={4} color="white" mt={8}>
      <Flex justifyContent="center" alignItems="center">
        <Text fontSize="sm" textAlign="center">
          © 2024 Stock Master. All rights reserved.
        </Text>
      </Flex>
    </Box>
  );
};

export default Footer;
