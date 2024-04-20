echo "Building..."

echo "" > ./viper.src

for i in $(ls ./libs);
do
    cat ./libs/$i >> ./viper.src
    echo "" >> ./viper.src
done

for i in $(ls ./functions);
do
    cat ./functions/$i >> ./viper.src
    echo "" >> ./viper.src
done

for i in $(ls ./core_commands);
do
    cat ./core_commands/$i >> ./viper.src
    echo "" >> ./viper.src
done

for i in $(ls ./commands);
do
    cat ./commands/$i >> ./viper.src
    echo "" >> ./viper.src
done

cat ./main/main.src >> ./viper.src

echo "Done building!"
