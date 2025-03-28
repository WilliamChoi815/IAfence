import React, { useEffect, useState } from "react";
import {
  Box,
  Heading,
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  Input,
  InputGroup,
  InputRightElement,
  IconButton,
  Flex,
  Button,
} from "@chakra-ui/react";
import { SearchIcon } from "@chakra-ui/icons";
import { useParams } from "react-router-dom";

function RankingsPage() {
  const { category } = useParams();
  const [rankings, setRankings] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [currentPage, setCurrentPage] = useState(1);

  const itemsPerPage = 10;

  useEffect(() => {
    const fetchRankings = async () => {
      try {
        const res = await fetch(
          `${process.env.REACT_APP_API_URL}/rankings/${
            category.charAt(0).toUpperCase() + category.slice(1)
          }/`
        );
        const data = await res.json();
        setRankings(data);
      } catch (error) {
        console.error("Error fetching full rankings:", error);
      }
    };

    fetchRankings();
  }, [category]);

  // Filtered results based on search
  const filteredRankings = rankings.filter((player) => {
    const name = player.player_name.toLowerCase();
    const team = player.affiliation.toLowerCase();
    const term = searchTerm.toLowerCase();
    return name.includes(term) || team.includes(term);
  });

  const totalPages = Math.ceil(filteredRankings.length / itemsPerPage);
  const startIndex = (currentPage - 1) * itemsPerPage;
  const paginatedData = filteredRankings.slice(
    startIndex,
    startIndex + itemsPerPage
  );

  return (
    <Box px={8} py={6} bg="gray.50" minH="100vh">
      {/* Section Header */}
      <Flex
        justify="space-between"
        align="center"
        pl={6}
        pr={8}
        py={4}
        flexWrap="wrap"
        gap={4}
      >
        <Heading size="lg" color="gray.800">
          Full Rankings
        </Heading>
        <InputGroup width="300px" bg="white">
          <Input
            placeholder="Search by player or team..."
            value={searchTerm}
            onChange={(e) => {
              setSearchTerm(e.target.value);
              setCurrentPage(1);
            }}
          />
          <InputRightElement>
            <IconButton
              icon={<SearchIcon />}
              size="md"
              colorScheme="gray"
              aria-label="Search"
              pointerEvents="none"
            />
          </InputRightElement>
        </InputGroup>
      </Flex>

      {/* Table */}
      <Box px={16} py={4} overflowX="auto">
        {paginatedData.length > 0 && (
          <Table variant="simple" size="md" bg="white" borderRadius="md">
            <Thead bg="gray.200">
              <Tr>
                <Th textAlign="center">Rank</Th>
                <Th textAlign="center">Player Name</Th>
                <Th textAlign="center">Age</Th>
                <Th textAlign="center">Affiliation</Th>
              </Tr>
            </Thead>
            <Tbody>
              {paginatedData.map((player) => (
                <Tr key={player.rank}>
                  <Td textAlign="center" fontWeight="bold">
                    #{player.rank}
                  </Td>
                  <Td textAlign="center">{player.player_name}</Td>
                  <Td textAlign="center">{player.age}</Td>
                  <Td textAlign="center">{player.affiliation}</Td>
                </Tr>
              ))}
            </Tbody>
          </Table>
        )}
      </Box>

      {/* Pagination Controls */}
      {totalPages > 1 && (
        <Flex justify="center" align="center" gap={2} mt={4} flexWrap="wrap">
          <Button
            onClick={() => setCurrentPage(1)}
            isDisabled={currentPage === 1}
            colorScheme="red"
            variant="outline"
            size="sm"
            fontWeight="bold"
          >
            &laquo;
          </Button>

          <Button
            onClick={() => setCurrentPage((p) => Math.max(p - 1, 1))}
            isDisabled={currentPage === 1}
            colorScheme="red"
            variant="outline"
            size="sm"
            fontWeight="bold"
          >
            &lsaquo;
          </Button>

          <Box fontWeight="bold" minW="100px" textAlign="center">
            Page {currentPage} of {totalPages}
          </Box>

          <Button
            onClick={() => setCurrentPage((p) => Math.min(p + 1, totalPages))}
            isDisabled={currentPage === totalPages}
            colorScheme="red"
            variant="outline"
            size="sm"
            fontWeight="bold"
          >
            &rsaquo;
          </Button>

          <Button
            onClick={() => setCurrentPage(totalPages)}
            isDisabled={currentPage === totalPages}
            colorScheme="red"
            variant="outline"
            size="sm"
            fontWeight="bold"
          >
            &raquo;
          </Button>
        </Flex>
      )}
    </Box>
  );
}

export default RankingsPage;
