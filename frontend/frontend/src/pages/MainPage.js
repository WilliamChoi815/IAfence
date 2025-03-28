import React from "react";
import { Box, Button, VStack, Heading, Text } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";

function MainPage() {
  const navigate = useNavigate();

  const handleNavigate = (category) => {
    navigate(`/category/${category}`);
  };

  return (
    <Box
      height="100vh"
      display="flex"
      flexDirection="column"
      bgGradient="linear(to-b, red.100, gray.50)"
    >
      {/* Header */}
      <Box
        p={6}
        textAlign="center"
        bgGradient="linear(to-r, gray.800, gray.600)"
        color="white"
        boxShadow="md"
      >
        <Heading fontSize={{ base: "4xl", md: "5xl" }} mb={2}>
          Fencing Competition Stat Website
        </Heading>
        <Text fontSize={{ base: "md", md: "lg" }} mt={2}>
          Track and analyze your fencing competitions
        </Text>
      </Box>

      {/* Buttons */}
      <Box flex="1" display="flex" justifyContent="center" alignItems="center">
        <VStack spacing={6}>
          {["sabre", "foil", "epee"].map((cat) => (
            <Button
              key={cat}
              onClick={() => handleNavigate(cat)}
              height={{ base: "80px", md: "100px" }}
              width={{ base: "250px", md: "300px" }}
              colorScheme="red"
              variant="solid"
              bg="red.500"
              color="white"
              fontSize={{ base: "2xl", md: "3xl" }}
              _hover={{
                bg: "red.600",
                transform: "scale(1.05)",
              }}
              transition="all 0.2s"
              boxShadow="lg"
            >
              {cat.charAt(0).toUpperCase() + cat.slice(1)}
            </Button>
          ))}
        </VStack>
      </Box>

      {/* Footer */}
      <Box
        p={4}
        textAlign="center"
        bgGradient="linear(to-r, gray.600, gray.800)"
        color="white"
        fontSize="sm"
        mt="auto"
      >
        © 2025 Fencing Stats. All rights reserved.
      </Box>
    </Box>
  );
}

export default MainPage;
