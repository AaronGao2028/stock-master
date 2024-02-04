import {
  Box,
  Button,
  Flex,
  HStack,
  Heading,
  Link,
  LinkBox,
  Spacer,
} from "@chakra-ui/react";

const Navbar = () => {
  return (
    <HStack
      z-index="999999"
      color="white"
      justify={"space-between"}
      background={"#add8e6"}
      right="0"
      left="0"
      top="0"
      height="60px"
      position="fixed"
    >
      <Link href="/">
        <Heading marginLeft="175px" fontSize={"30px"} fontFamily={"Arial"}>
          STOCK MASTER
        </Heading>
      </Link>
      <HStack spacing={5} marginRight="50px" fontSize={"20px"}>
        <Link href="/how-it-works">How it works</Link>
        <Link href="/creation-story">Creation Story</Link>
        <Button backgroundColor="beige">Login</Button>
      </HStack>
    </HStack>
  );
};

export default Navbar;
