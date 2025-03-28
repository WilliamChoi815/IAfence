import React from "react";
import {
  Box,
  Flex,
  Button,
  IconButton,
  Input,
  InputGroup,
  InputRightElement,
} from "@chakra-ui/react";
import { useLocation, useNavigate } from "react-router-dom";
import { SearchIcon } from "@chakra-ui/icons";

const categories = ["sabre", "foil", "epee"];

function Header() {
  const location = useLocation();
  const navigate = useNavigate();
  const currentCategory = location.pathname.split("/")[2];

  return (
    <Box
      bgGradient="linear(to-r, gray.800, gray.600)"
      color="white"
      px={10}
      py={5}
      boxShadow="md"
    >
      <Flex align="center" justify="space-between" wrap="wrap">
        {/* Left: Category buttons */}
        <Flex gap={10}>
          {categories.map((cat) => (
            <Button
              key={cat}
              onClick={() => navigate(`/category/${cat}`)}
              variant={currentCategory === cat ? "solid" : "ghost"}
              colorScheme="red"
              size="md"
              fontSize={{ base: "md", md: "lg" }}
              fontWeight="bold"
            >
              {cat.charAt(0).toUpperCase() + cat.slice(1)}
            </Button>
          ))}
        </Flex>

        {/* Right: Search + Admin */}
        <Flex gap={5} align="center" mt={{ base: 4, md: 0 }}>
          <InputGroup minW="400px">
            <Input placeholder="Search..." bg="white" color="black" />
            <InputRightElement>
              <IconButton
                icon={<SearchIcon />}
                size="md"
                colorScheme="gray"
                aria-label="Search"
                fontSize={{ base: "md", md: "lg" }}
              />
            </InputRightElement>
          </InputGroup>

          <Button
            size="md"
            colorScheme="red"
            variant="outline"
            fontWeight="bold"
            fontSize={{ base: "md", md: "lg" }}
          >
            Admin
          </Button>
        </Flex>
      </Flex>
    </Box>
  );
}

export default Header;
